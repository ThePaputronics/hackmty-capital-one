import React from 'react';
import { theme } from '../theme';
import { DecisionBadge } from '../components/DecisionBadge';

export const Thumbnail: React.FC = () => {
  return (
    <div
      style={{
        width: 1920,
        height: 1080,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '0 120px',
        position: 'relative',
        overflow: 'hidden',
        boxSizing: 'border-box',
      }}
    >
      {/* Background ambient lighting/glow */}
      <div
        style={{
          position: 'absolute',
          top: -200,
          left: -150,
          width: 700,
          height: 700,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(216, 155, 66, 0.15) 0%, transparent 70%)',
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -200,
          right: -100,
          width: 800,
          height: 800,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(239, 68, 68, 0.12) 0%, transparent 70%)',
          pointerEvents: 'none',
        }}
      />

      {/* Left Column: Branding, Value Prop & Key Metrics */}
      <div style={{ display: 'flex', flexDirection: 'column', maxWidth: '950px', zIndex: 2 }}>
        {/* Challenge / Category Pill */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px', marginBottom: '24px' }}>
          <span
            style={{
              backgroundColor: 'rgba(216, 155, 66, 0.15)',
              border: `1.5px solid ${theme.colors.accent}`,
              borderRadius: '8px',
              padding: '8px 18px',
              color: theme.colors.accentLight,
              fontFamily: theme.fonts.mono,
              fontSize: '15px',
              fontWeight: 700,
              letterSpacing: '2px',
              textTransform: 'uppercase',
            }}
          >
            Capital One Challenge · Real-Time Anomaly Sentinel
          </span>
          <DecisionBadge decision="pause" size="sm" />
        </div>

        {/* Project Name */}
        <h1
          style={{
            fontSize: '110px',
            fontFamily: theme.fonts.serif,
            fontWeight: 700,
            letterSpacing: '6px',
            color: '#ffffff',
            margin: '0 0 16px 0',
            lineHeight: 1,
            textShadow: '0 0 40px rgba(255, 255, 255, 0.15)',
          }}
        >
          F.R.E.D
        </h1>

        {/* Subtitle / Core Hook */}
        <p
          style={{
            fontSize: '36px',
            lineHeight: 1.35,
            color: '#e2e8f0',
            fontFamily: theme.fonts.serif,
            fontWeight: 400,
            margin: '0 0 44px 0',
          }}
        >
          Protección en tiempo real contra fraudes por manipulación antes de la liquidación SPEI.
        </p>

        {/* Highlight Stat Badges */}
        <div style={{ display: 'flex', gap: '20px' }}>
          <div
            style={{
              backgroundColor: theme.colors.card,
              border: `1.5px solid ${theme.colors.cardBorder}`,
              borderRadius: '14px',
              padding: '18px 26px',
              display: 'flex',
              flexDirection: 'column',
            }}
          >
            <span style={{ color: theme.colors.accentLight, fontFamily: theme.fonts.mono, fontSize: '32px', fontWeight: 800 }}>
              6 / 6
            </span>
            <span style={{ color: theme.colors.textMuted, fontFamily: theme.fonts.sans, fontSize: '14px', marginTop: '4px' }}>
              Ataques APP interceptados
            </span>
          </div>

          <div
            style={{
              backgroundColor: theme.colors.card,
              border: `1.5px solid ${theme.colors.cardBorder}`,
              borderRadius: '14px',
              padding: '18px 26px',
              display: 'flex',
              flexDirection: 'column',
            }}
          >
            <span style={{ color: theme.colors.allow, fontFamily: theme.fonts.mono, fontSize: '32px', fontWeight: 800 }}>
              0.0%
            </span>
            <span style={{ color: theme.colors.textMuted, fontFamily: theme.fonts.sans, fontSize: '14px', marginTop: '4px' }}>
              Falsos positivos (PyMEs)
            </span>
          </div>

          <div
            style={{
              backgroundColor: theme.colors.card,
              border: `1.5px solid ${theme.colors.cardBorder}`,
              borderRadius: '14px',
              padding: '18px 26px',
              display: 'flex',
              flexDirection: 'column',
            }}
          >
            <span style={{ color: '#60a5fa', fontFamily: theme.fonts.mono, fontSize: '32px', fontWeight: 800 }}>
              &lt; 4 ms
            </span>
            <span style={{ color: theme.colors.textMuted, fontFamily: theme.fonts.sans, fontSize: '14px', marginTop: '4px' }}>
              Latencia p95 reproducible
            </span>
          </div>
        </div>
      </div>

      {/* Right Column: Visual Mockup of Mobile Active Intercept */}
      <div
        style={{
          transform: 'rotate(-4deg) scale(0.95)',
          filter: 'drop-shadow(0 30px 60px rgba(0, 0, 0, 0.9)) drop-shadow(0 0 35px rgba(239, 68, 68, 0.35))',
          zIndex: 3,
        }}
      >
        <div
          style={{
            width: '380px',
            height: '660px',
            backgroundColor: '#0a0c10',
            borderRadius: '40px',
            border: '4px solid #3b4257',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
            fontFamily: theme.fonts.sans,
            position: 'relative',
          }}
        >
          {/* Dynamic Island */}
          <div
            style={{
              width: '110px',
              height: '22px',
              backgroundColor: '#161922',
              margin: '12px auto 6px auto',
              borderRadius: '14px',
            }}
          />

          {/* Header */}
          <div
            style={{
              padding: '10px 20px',
              borderBottom: '1px solid #202433',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <span style={{ color: '#fff', fontWeight: 600, fontSize: '14px' }}>Banca Móvil</span>
            <span style={{ color: '#888e9f', fontSize: '12px' }}>SPEI En Vivo</span>
          </div>

          {/* Transfer Info */}
          <div style={{ padding: '20px', flex: 1, display: 'flex', flexDirection: 'column' }}>
            <div style={{ color: '#8e94a5', fontSize: '12px', textTransform: 'uppercase' }}>
              Transferencia en curso
            </div>
            <div style={{ color: '#ffffff', fontSize: '34px', fontWeight: 700, fontFamily: theme.fonts.mono, margin: '4px 0 14px 0' }}>
              $12,450.00 <span style={{ fontSize: '14px', color: '#888' }}>MXN</span>
            </div>

            <div style={{ backgroundColor: '#141721', padding: '10px 12px', borderRadius: '8px', marginBottom: '16px', border: '1px solid #242938' }}>
              <div style={{ fontSize: '11px', color: '#888e9f' }}>Destinatario</div>
              <div style={{ color: '#e2e5ec', fontSize: '12px', fontFamily: theme.fonts.mono, marginTop: '2px' }}>
                646180157088992112
              </div>
              <div style={{ fontSize: '11px', color: '#d89b42', marginTop: '3px' }}>
                STP · Beneficiario no habitual (&lt; 15 min)
              </div>
            </div>

            {/* Warning Intercept */}
            <div
              style={{
                backgroundColor: 'rgba(239, 68, 68, 0.14)',
                border: '1.5px solid #ef4444',
                borderRadius: '12px',
                padding: '14px',
                marginBottom: '16px',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                <span style={{ fontSize: '16px' }}>⚠️</span>
                <span style={{ color: '#ef4444', fontWeight: 800, fontSize: '13px', letterSpacing: '0.5px' }}>
                  PAUSA POR RIESGO DE ENGAÑO
                </span>
              </div>
              <div style={{ color: '#fca5a5', fontSize: '12px', lineHeight: 1.4 }}>
                Detectamos una llamada telefónica activa simultánea. Los bancos nunca piden transferencias por llamada.
              </div>
            </div>

            {/* Cancelled Button */}
            <div style={{ marginTop: 'auto' }}>
              <div
                style={{
                  padding: '12px',
                  backgroundColor: '#ef4444',
                  borderRadius: '10px',
                  color: '#ffffff',
                  fontWeight: 800,
                  fontSize: '13px',
                  textAlign: 'center',
                  letterSpacing: '0.5px',
                  boxShadow: '0 0 20px rgba(239, 68, 68, 0.5)',
                }}
              >
                ✓ $12,450.00 MXN PROTEGIDOS
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer bar */}
      <div
        style={{
          position: 'absolute',
          bottom: '30px',
          left: '120px',
          right: '120px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderTop: `1px solid ${theme.colors.surfaceBorder}`,
          paddingTop: '16px',
          color: theme.colors.textMuted,
          fontFamily: theme.fonts.mono,
          fontSize: '14px',
        }}
      >
        <span>sixsevencitos.tech</span>
        <span>Banco de México (SPEI) · HackMTY 2026</span>
      </div>
    </div>
  );
};
