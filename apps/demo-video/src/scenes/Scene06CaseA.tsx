import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';
import { DecisionBadge } from '../components/DecisionBadge';
import simulationData from '../data/simulation.json';

export const Scene06CaseA: React.FC = () => {
  const frame = useCurrentFrame();
  const caseA = simulationData.case_a;

  const cardOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const badgeScale = interpolate(frame, [25, 45], [0.8, 1], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        padding: '0 120px',
      }}
    >
      <div style={{ marginBottom: '35px' }}>
        <span style={{ color: theme.colors.allow, fontFamily: theme.fonts.mono, fontSize: '15px', letterSpacing: '2px', textTransform: 'uppercase' }}>
          Caso A · Transferencia Legítima
        </span>
        <h2 style={{ color: '#fff', fontFamily: theme.fonts.serif, fontSize: '46px', margin: '6px 0 0 0' }}>
          Monto alto pero con beneficiario y contexto habitual
        </h2>
      </div>

      <div
        style={{
          opacity: cardOpacity,
          backgroundColor: theme.colors.surface,
          border: `1px solid ${theme.colors.surfaceBorder}`,
          borderRadius: '16px',
          padding: '40px',
          display: 'grid',
          gridTemplateColumns: '1.2fr 1fr',
          gap: '40px',
          alignItems: 'center',
        }}
      >
        <div>
          <div style={{ display: 'flex', gap: '20px', alignItems: 'baseline', marginBottom: '20px' }}>
            <span style={{ color: '#fff', fontSize: '50px', fontFamily: theme.fonts.mono, fontWeight: 700 }}>
              ${caseA.amount.toLocaleString('es-MX', { minimumFractionDigits: 2 })} <span style={{ fontSize: '20px', color: '#888' }}>MXN</span>
            </span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', color: theme.colors.textSecondary, fontSize: '16px' }}>
            <div><strong>Ordenante:</strong> <code style={{ color: theme.colors.accentLight }}>{caseA.payer_id}</code> (Comercio PYME)</div>
            <div><strong>Destinatario:</strong> <code style={{ color: '#fff' }}>{caseA.destination_clabe}</code></div>
            <div><strong>Historial:</strong> Beneficiario transferido previamente durante el período de warmup.</div>
            <div><strong>Sesión:</strong> Dispositivo e IP habituales, sin llamada activa.</div>
          </div>
        </div>

        <div
          style={{
            backgroundColor: '#121620',
            border: `1px solid ${theme.colors.border}`,
            borderRadius: '12px',
            padding: '30px',
            textAlign: 'center',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <div style={{ color: theme.colors.textMuted, fontSize: '13px', fontFamily: theme.fonts.mono, marginBottom: '16px' }}>
            CORROBORACIÓN DE SEÑALES
          </div>
          <div style={{ transform: `scale(${badgeScale})`, marginBottom: '16px' }}>
            <DecisionBadge decision="allow" size="lg" />
          </div>
          <div style={{ color: theme.colors.allow, fontSize: '16px', fontWeight: 600 }}>
            Sin fricción innecesaria
          </div>
          <div style={{ color: theme.colors.textMuted, fontSize: '14px', marginTop: '6px' }}>
            Una sola señal elevada (monto) nunca bloquea al cliente.
          </div>
        </div>
      </div>
    </div>
  );
};
