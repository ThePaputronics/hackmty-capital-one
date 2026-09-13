import React from 'react';
import { theme } from '../theme';

interface PhoneCardProps {
  amount: number;
  recipientClabe: string;
  recipientBank: string;
  payerMessage: string;
  visibleChars?: number;
  isCancelled?: boolean;
}

export const PhoneCard: React.FC<PhoneCardProps> = ({
  amount,
  recipientClabe,
  recipientBank,
  payerMessage,
  visibleChars = payerMessage.length,
  isCancelled = false,
}) => {
  const displayedMessage = payerMessage.slice(0, visibleChars);

  return (
    <div
      style={{
        width: '380px',
        height: '740px',
        backgroundColor: '#0a0c10',
        borderRadius: '44px',
        border: '4px solid #33394a',
        boxShadow: '0 25px 60px rgba(0,0,0,0.8), 0 0 40px rgba(239, 68, 68, 0.2)',
        overflow: 'hidden',
        display: 'flex',
        flexDirection: 'column',
        fontFamily: theme.fonts.sans,
        position: 'relative',
      }}
    >
      {/* Notch / Dynamic Island */}
      <div
        style={{
          width: '120px',
          height: '24px',
          backgroundColor: '#161922',
          margin: '12px auto 6px auto',
          borderRadius: '16px',
        }}
      />

      {/* App Header */}
      <div
        style={{
          padding: '12px 20px',
          borderBottom: '1px solid #202433',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <span style={{ color: '#fff', fontWeight: 600, fontSize: '15px' }}>Banca Móvil</span>
        <span style={{ color: '#888e9f', fontSize: '12px' }}>SPEI</span>
      </div>

      {/* Transfer detail */}
      <div style={{ padding: '24px 20px', flex: 1, display: 'flex', flexDirection: 'column' }}>
        <div style={{ color: '#8e94a5', fontSize: '13px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
          Transferencia propuesta
        </div>
        <div style={{ color: '#ffffff', fontSize: '36px', fontWeight: 700, fontFamily: theme.fonts.mono, margin: '6px 0 16px 0' }}>
          ${amount.toLocaleString('es-MX', { minimumFractionDigits: 2 })} <span style={{ fontSize: '16px', color: '#888' }}>MXN</span>
        </div>

        <div style={{ backgroundColor: '#141721', padding: '12px 14px', borderRadius: '8px', marginBottom: '20px', border: '1px solid #242938' }}>
          <div style={{ fontSize: '12px', color: '#888e9f' }}>Destinatario</div>
          <div style={{ color: '#e2e5ec', fontSize: '13px', fontFamily: theme.fonts.mono, marginTop: '2px' }}>
            {recipientClabe}
          </div>
          <div style={{ fontSize: '11px', color: '#d89b42', marginTop: '4px' }}>
            {recipientBank} · Primera vez
          </div>
        </div>

        {/* Warning / Intervention Modal */}
        <div
          style={{
            backgroundColor: 'rgba(239, 68, 68, 0.12)',
            border: '1.5px solid #ef4444',
            borderRadius: '12px',
            padding: '16px',
            marginBottom: '16px',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
            <span style={{ fontSize: '18px' }}>⚠️</span>
            <span style={{ color: '#ef4444', fontWeight: 700, fontSize: '14px', letterSpacing: '0.5px' }}>
              TRANSFERENCIA EN PAUSA
            </span>
          </div>
          <div style={{ color: '#fca5a5', fontSize: '13px', lineHeight: 1.45 }}>
            {displayedMessage}
          </div>
        </div>

        <div style={{ marginTop: 'auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <button
            style={{
              padding: '14px',
              backgroundColor: isCancelled ? '#ef4444' : '#222736',
              border: isCancelled ? '1px solid #ef4444' : '1px solid #3b4257',
              borderRadius: '10px',
              color: '#ffffff',
              fontWeight: 700,
              fontSize: '14px',
              cursor: 'pointer',
              transition: 'all 0.2s ease',
            }}
          >
            {isCancelled ? '✓ TRANSFERENCIA CANCELADA' : 'Cancelar transferencia'}
          </button>
          {!isCancelled && (
            <button
              style={{
                padding: '12px',
                backgroundColor: 'transparent',
                border: 'none',
                color: '#6e7488',
                fontSize: '12px',
              }}
            >
              Llamar a mi banco oficial
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
